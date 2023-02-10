import divide
import cv2
import predict
import translate

img = cv2.imread("C:\\Users\\Firas\\Downloads\\chess.com2.png")
images = divide.divideBoard(img)
labels = predict.prediction(images)
fen = translate.toFEN(labels)

print(labels)
print(fen)