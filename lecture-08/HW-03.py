from datetime import datetime

def analyze_user_activity(log_file_path: str) -> dict:
    users = {}
    action_counts = {}
    session_times = {}

    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 4:
                continue

            timestamp_str, user_id, action, duration_str = parts
            try:
                datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")
                duration = int(duration_str)
            except ValueError:
                continue

            # นับ action
            action_counts[action] = action_counts.get(action, 0) + 1

            # รวมเวลาที่เกี่ยวข้อง (เฉพาะ login, submit, logout)
            if action in ("login", "submit", "logout"):
                session_times[user_id] = session_times.get(user_id, 0) + duration

            # เก็บผู้ใช้
            users[user_id] = True

    if not users:
        return {
            "total_users": 0,
            "action_counts": {},
            "most_active_user": None,
            "average_session_time": 0.0
        }

    most_active_user = max(session_times, key=session_times.get)
    avg_session_time = sum(session_times.values()) / len(session_times)

    return {
        "total_users": len(users),
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": avg_session_time
    }
