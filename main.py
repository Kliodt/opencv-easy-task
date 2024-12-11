import cv2

def main():
    win_title = "Lab 4"
    box_size = 50
    
    # Подключение к камере (0 - основная камера)
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: can't open camera")
        cam.release()
        return

    while True:
        # Чтение кадра с камеры
        success, frame = cam.read()
        if not success:
            print("Error: can't read the frame")
            break

        # Координаты рамок
        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2

        box_1 = [(center_x - 2 * box_size, center_y - box_size // 2),
                 (center_x - box_size, center_y + box_size // 2)]
        
        box_2 = [(center_x - box_size, center_y - box_size // 2),
                 (center_x, center_y + box_size // 2)]
        
        box_3 = [(center_x, center_y - box_size // 2),
                 (center_x + box_size, center_y + box_size // 2)]
        
        box_4 = [(center_x + box_size, center_y - box_size // 2),
                 (center_x + 2 * box_size, center_y + box_size // 2)]
        
        boxes =  [box_1, box_2, box_3, box_4]

        # определение цветов внутри box
        for i in range(len(boxes)):
            box = boxes[i]
            top_left = box[0]
            bottom_right = box[1]

            # часть кадра внутри box
            box_in = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            mean_color = cv2.mean(box_in)
            mean_color_bgr = mean_color[:3]
            
            text = f"{i}: BGR({int(mean_color_bgr[0])}, {int(mean_color_bgr[1])}, {int(mean_color_bgr[2])})"
            cv2.putText(frame, text, (10, 30 * (i+1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            
        # отрисовка box
        for box in boxes:
            top_left = box[0]
            bottom_right = box[1]
            cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), 2)


        # Отображение кадра
        cv2.imshow(win_title, frame)

        # Проверка на закрытие окна
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or cv2.getWindowProperty(win_title, cv2.WND_PROP_VISIBLE) < 1:
            break

    # Освобождение ресурсов
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
