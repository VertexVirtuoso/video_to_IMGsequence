import os
import subprocess
import sys

def convert_video_to_proxy_images(input_file_path, output_dir_path):
    # Get the file name and remove the file extension
    file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))

    # Create the directory for the proxy images
    output_dir_path = os.path.join(output_dir_path, f"{file_name}_proxy")
    os.makedirs(output_dir_path, exist_ok=True)

    # Convert the video to a sequence of proxy images
    proxy_image_pattern = os.path.join(output_dir_path, f"animatic.%04d.jpg")
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            input_file_path,
            "-vf",
            "scale=720:-1",
            "-r",
            "24",
            proxy_image_pattern,
        ]
    )


if __name__ == "__main__":
    # Get the input and output paths from the command-line arguments
    input_file_path = sys.argv[1]
    output_dir_path = sys.argv[2]

    # Convert the video to a sequence of proxy images
    convert_video_to_proxy_images(input_file_path, output_dir_path)
