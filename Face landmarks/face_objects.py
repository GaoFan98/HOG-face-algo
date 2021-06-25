import PIL.Image
import PIL.ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("photos/test_2.jpeg")

face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print("Number of faces on photo is => {}".format(number_of_faces))

pil_image = PIL.Image.fromarray(image)

draw = PIL.ImageDraw.Draw(pil_image)

# Loop over each face
for face_landmarks in face_landmarks_list:

    # Loop over each facial feature
    for name, list_of_points in face_landmarks.items():
        # Print the location of each facial feature in this image
        print("The {} in this face has the following points: {}".format(name, list_of_points))

        # Let's trace out each facial feature in the image with a line!
        draw.line(list_of_points, fill="red", width=2)

pil_image.show()
