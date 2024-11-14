# game_tracker.py
from detection.player_detector import PlayerDetector
from detection.basketball_detector import BasketballDetector
from action_detection.action_classifier import ActionClassifier
from action_detection.shot_detector import ShotDetector

class GameTracker:
    def __init__(self, model_paths):
        self.player_detector = PlayerDetector(model_paths['player'])
        self.basketball_detector = BasketballDetector(model_paths['basketball'])
        self.action_classifier = ActionClassifier()
        self.shot_detector = ShotDetector()

    def track_game(self, video_path):
        # Process the video frame-by-frame
        video = cv2.VideoCapture(video_path)
        game_data = []

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            players = self.player_detector.detect_players(frame)
            basketball = self.basketball_detector.detect_basketball(frame)

            # Example data structure for tracking actions and possessions
            game_data.append({
                'players': players,
                'basketball': basketball,
                # Track and classify actions here, update shot results
            })

        video.release()
        return game_data
