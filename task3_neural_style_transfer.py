import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2

def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img

def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return tensor

def apply_style_transfer(content_path, style_path, output_path):
    print(f"Loading content ({content_path}) and style ({style_path}) images...")
    try:
        content_image = load_img(content_path)
        style_image = load_img(style_path)
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    print("Loading TF Hub Arbitrary Image Stylization model...")
    # Load the pre-trained model from TensorFlow Hub
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    print("Applying style transfer (this might take a moment)...")
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]

    final_image = tensor_to_image(stylized_image)

    # Convert RGB to BGR for OpenCV saving
    final_image_bgr = cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, final_image_bgr)
    print(f"Stylized image successfully saved to {output_path}")

if __name__ == "__main__":
    print("=== CODTECH Task 3: Neural Style Transfer ===")
    print("Please make sure you have 'content.jpg' and 'style.jpg' in your directory.")
    
    # Defaults
    content_file = "content.jpg"
    style_file = "style.jpg"
    output_file = "stylized_output.jpg"
    
    # Try running the style transfer
    apply_style_transfer(content_file, style_file, output_file)
