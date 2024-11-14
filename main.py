# main.py
from game_analysis.game_tracker import GameTracker
import json

def main(video_path):
    model_paths = {
        'player': 'path/to/player/model',
        'basketball': 'path/to/basketball/model'
    }
    
    game_tracker = GameTracker(model_paths)
    game_data = game_tracker.track_game(video_path)

    # Output results
    with open("game_summary.json", "w") as outfile:
        json.dump(game_data, outfile)

if __name__ == "__main__":
    video_path = "path/to/basketball_game.mp4"
    main(video_path)
