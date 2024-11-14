# main.py
from detection.player_detector import PlayerDetector
from detection.basketball_detector import BasketballDetector
import cv2

def main(video_path):
    player_detector = PlayerDetector('path/to/yolov8n.pt')
    basketball_detector = BasketballDetector('path/to/yolov8n.pt')

    # Open video file
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect players and basketball
        players = player_detector.detect_players(frame)
        basketball = basketball_detector.detect_basketball(frame)

        # Display results (bounding boxes)
        for player in players:
            x1, y1, x2, y2 = player['bbox']
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box for players

        for ball in basketball:
            x1, y1, x2, y2 = ball['bbox']
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red box for basketball

        # Show frame with detections
        cv2.imshow("Basketball Action Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main("path/to/basketball_game.mp4")
