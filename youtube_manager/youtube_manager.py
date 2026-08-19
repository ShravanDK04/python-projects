import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return

    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")


def add_video(videos):
    name = input("Enter video title: ").strip()

    if not name:
        print("Video title cannot be empty.")
        return

    time = input("Enter video duration: ").strip()

    if not time:
        print("Video duration cannot be empty.")
        return

    videos.append({
        'name': name,
        'time': time
    })

    save_data_helper(videos)
    print("Video added successfully.")


def update_video(videos):
    if not videos:
        print("No videos found.")
        return

    list_all_videos(videos)

    try:
        index = int(input("Enter the video index to be updated: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= index <= len(videos):

        new_name = input("Enter new video title: ").strip()

        if not new_name:
            print("Video title cannot be empty.")
            return

        new_duration = input("Enter new video duration: ").strip()

        if not new_duration:
            print("Video duration cannot be empty.")
            return

        videos[index - 1] = {
            'name': new_name,
            'time': new_duration
        }

        save_data_helper(videos)
        print("Video updated successfully.")

    else:
        print("Invalid index selected.")


def delete_video(videos):
    if not videos:
        print("No videos found.")
        return

    list_all_videos(videos)

    try:
        index = int(input("Enter video index to be deleted: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= index <= len(videos):
        deleted_video = videos.pop(index - 1)

        save_data_helper(videos)

        print(f"'{deleted_video['name']}' deleted successfully.")

    else:
        print("Invalid index selected.")


def search_videos(videos):
    if not videos:
        print("No videos found.")
        return

    search = input("Enter video title to search: ").strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    found = 0

    for index, video in enumerate(videos, start=1):
        if search in video['name'].lower():
            print(f"{index}. {video['name']}, Duration: {video['time']}")
            found += 1

    if found == 0:
        print("No videos found.")
    else:
        print(f"Found {found} video(s).")


def sort_videos(videos):
    if not videos:
        print("No videos available to sort.")
        return

    print("\nSort Videos")
    print("1. Title (A-Z)")
    print("2. Title (Z-A)")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        return

    if choice == 1:
        sorted_videos = sorted(
            videos,
            key=lambda video: video['name'].lower()
        )

    elif choice == 2:
        sorted_videos = sorted(
            videos,
            key=lambda video: video['name'].lower(),
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    list_all_videos(sorted_videos)


def main():

    videos = load_data()

    while True:

        print("\n========== YouTube Manager ==========")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Search videos")
        print("6. Sort videos")
        print("7. Exit application")
        print("=====================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:

            case 1:
                list_all_videos(videos)

            case 2:
                add_video(videos)

            case 3:
                update_video(videos)

            case 4:
                delete_video(videos)

            case 5:
                search_videos(videos)

            case 6:
                sort_videos(videos)

            case 7:
                print("Thank you for using YouTube Manager.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()