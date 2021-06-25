import face_recognition
from pathlib import Path
from PIL import Image

# Load the image of the person we want to find similar people for
known_image = face_recognition.load_image_file("test.jpg")
# Encode the known image
known_image_encoding = face_recognition.face_encodings(known_image)[0]
# Variables to keep track of the most similar face match we've found
best_face_distance = 1.0
best_face_image = None
# get both png and jpg format photos
types = ('*.png', '*.jpg')

counter = 0
for type in types:
    for image_path in Path("people").glob(type):
        counter += 1
        unknown_image = face_recognition.load_image_file(image_path)
        print("Checking the photo number {}".format(counter))

        face_encodings = face_recognition.face_encodings(unknown_image)
        # Get the face distance between the known person and all the faces in this image
        face_distance = face_recognition.face_distance(face_encodings, known_image_encoding)[0]
        # If this face is more similar to our known image than we've seen so far, save it
        if face_distance < best_face_distance:
            # Save the new best face distance
            best_face_distance = face_distance
            # Extract a copy of the actual face image itself so we can display it
            best_face_image = unknown_image

pil_image = Image.fromarray(best_face_image)
pil_image.show()
