import json
import re
from pathlib import Path

class UserProfile:
    def __init__(self, user_id="default"):
        sanitized_user_id = re.sub(r'[^a-zA-Z0-9_-]', '_', user_id)
        self.user_id = sanitized_user_id
        self.profile_path = Path(f"user_profiles/{sanitized_user_id}.json")
        self.data = None
        self.ensure_data_loaded()

    def ensure_data_loaded(self):
        """Ensure profile data is loaded"""
        if self.data is None:
            self.load_profile()

    def load_profile(self):
        """Load existing profile from JSON"""
        try:
            if self.profile_path.exists():
                with open(self.profile_path, 'r') as f:
                    self.data = json.load(f)
            else:
                self.data = {
                    "topics": {
                        "arithmetic": {"correct": 0, "incorrect": 0},
                        # Initialize other topics similarly
                    }
                }
        except Exception as e:
            print(f"Failed to load profile: {e}")
            self.data = {"topics": {}}

    def save_profile(self):
        """Save profile to JSON file"""
        try:
            self.profile_path.parent.mkdir(exist_ok=True)
            with open(self.profile_path, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Failed to save profile: {e}")

    def update_topic(self, topic: str, is_correct: bool):
        self.ensure_data_loaded()
        if topic not in self.data["topics"]:
            self.data["topics"][topic] = {"correct": 0, "incorrect": 0}
        
        if is_correct:
            self.data["topics"][topic]["correct"] += 1
        else:
            self.data["topics"][topic]["incorrect"] += 1

        self.save_profile()
