import cv2

image_path = "opossum.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Зображення не знайдено. Перевір шлях.")
else:
    print("Зображення успішно завантажене")

print("Розмір зображення:", image.shape)
print("Тип даних:", image.dtype)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

mean_per_channel = image_rgb.mean(axis=(0, 1))
min_per_channel = image_rgb.min(axis=(0, 1))
max_per_channel = image_rgb.max(axis=(0, 1))

print("Середнє по каналах (R, G, B):", mean_per_channel)
print("Мінімальні значення (R, G, B):", min_per_channel)
print("Максимальні значення (R, G, B):", max_per_channel)

total_intensity = image_rgb.sum()
print("Загальна інтенсивність пікселів:", total_intensity)

normalized_image = image_rgb / 255.0
print("Перші 5 нормалізованих пікселів:\n", normalized_image.reshape(-1, 3)[:5])