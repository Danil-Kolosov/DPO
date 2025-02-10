import cv2
import numpy as np
import torch

# Загрузка конфигурационного файла и весов
net = cv2.dnn.readNetFromDarknet('../Configure\\neuronNet.cfg','../Configure\\neuronNet.weights')

# Загрузка классов
with open('../Configure\\objects.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Загрузка изображения
image = cv2.imread('../Images\\image3.jpg')
height, width, _ = image.shape

# Подготовка изображения к обработке моделью
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)

# Получение предсказаний
output_layers = net.getUnconnectedOutLayersNames()
outs = net.forward(output_layers)

# Обработка результатов
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Фильтрация по порогу уверенности
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Прямоугольник вокруг объекта
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Применение Non-Maxima Suppression для удаления дубликатов
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Отображение результатов на изображении
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Показываем изображение
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()