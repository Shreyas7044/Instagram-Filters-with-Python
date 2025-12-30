from instafilter import Instafilter
import cv2

def apply_filter(image_path, filter_name="Lo-fi", output_name="modified_image.jpg"):
    try:
        print(f"Applying {filter_name} filter...")
        model = Instafilter(filter_name)
        new_image = model(image_path)
        cv2.imwrite(output_name, new_image)
        print(f"Filter applied successfully! Saved as {output_name}")
    except Exception as e:
        print("Error:", e)
        print("Make sure the image exists and libraries are installed properly.")

if __name__ == "__main__":
    # Change the image name & filter if needed
    input_image = "image.jpg"      # Place your image in same folder
    filter_to_apply = "Lo-fi"      # Try: "Clarendon","Gingham","Moon","Lark"
    output_file = "filtered_image.jpg"

    apply_filter(input_image, filter_to_apply, output_file)