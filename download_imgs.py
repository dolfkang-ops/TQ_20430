import urllib.request
import os

os.makedirs('images', exist_ok=True)

img_urls = [
    ('map.jpg', 'https://image.thankqcamping.com/file/2026/10/24/515edc4e-434d-4f7e-973f-e66f8234dd55.jpg'),
    ('camp1.jpg', 'https://image.thankqcamping.com/file/2026/08/19/e73df56f-8795-4890-a36e-34c00f176bd7.jpg'),
    ('camp2.jpg', 'https://image.thankqcamping.com/file/2026/08/19/2a94d496-c68b-4869-a672-bd13bddb1056.jpg'),
    ('camp3.jpg', 'https://image.thankqcamping.com/file/2026/08/19/256b24b7-b84f-4bf3-bea4-59a77f310cbb.jpg'),
    ('camp4.jpg', 'https://image.thankqcamping.com/file/2026/08/19/e4d71e50-6df0-41e0-a9cf-98e9ab9d6550.jpg'),
    ('camp5.jpg', 'https://image.thankqcamping.com/file/2026/08/19/5c6a1874-af92-4a90-8de4-5aa49d1d23ee.jpg'),
    ('camp6.jpg', 'https://image.thankqcamping.com/file/2026/08/19/3183107e-9bb5-4bec-9ca7-b15760b47fff.jpg'),
    ('camp7.jpg', 'https://image.thankqcamping.com/file/2026/08/19/18b42791-3c49-4092-ba00-c283685d6aa3.jpg'),
    ('camp8.jpg', 'https://image.thankqcamping.com/file/2026/08/19/7c612428-4c3c-46d0-ac00-658268f90a95.jpg'),
    ('camp9.jpg', 'https://image.thankqcamping.com/file/2026/08/19/1c4f9e0c-4c56-4912-a338-a7db7588f9f5.jpg'),
    ('camp10.jpg', 'https://image.thankqcamping.com/file/2026/08/19/45f8594b-3cb8-471c-a8cf-716cd0b17d5b.jpg'),
    ('camp11.jpg', 'https://image.thankqcamping.com/file/2026/08/19/f32b9a25-39c1-42b0-b5fb-52e6909ec695.jpg'),
    ('camp12.jpg', 'https://image.thankqcamping.com/file/2026/08/19/7132e002-b89d-4a18-97e3-08112f364a63.jpg'),
    ('camp13.jpg', 'https://image.thankqcamping.com/file/2026/08/19/8ea61bff-ff98-4073-bc80-ffb126167b10.jpg'),
    ('camp14.jpg', 'https://image.thankqcamping.com/file/2026/08/19/513f06e5-5516-4b79-8290-47c04c6a2cf3.jpg'),
    ('camp15.jpg', 'https://image.thankqcamping.com/file/2026/08/19/26661c1d-58e0-433d-ba72-945804aa1913.jpg'),
    ('camp16.jpg', 'https://image.thankqcamping.com/file/2026/08/19/8f558d16-3a8c-4de8-aa33-9070a7f122e5.jpg'),
    ('camp17.jpg', 'https://image.thankqcamping.com/file/2026/08/19/9c831c32-2eda-47ad-9b99-f82578a57322.jpg')
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in img_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(os.path.join('images', name), 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {name} ({os.path.getsize(os.path.join('images', name))} bytes)")
    except Exception as e:
        print(f"Failed {name}: {e}")
