import os
import hashlib
import shutil

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def main():
    origin_dir = "originmaps"
    output_dir = "outmaps"

    if not os.path.exists(origin_dir):
        print(f"错误：源目录 '{origin_dir}' 不存在！")
        return

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(origin_dir):
        if filename.lower().endswith(".map"):
            original_filepath = os.path.join(origin_dir, filename)

            if not os.path.isfile(original_filepath):
                continue

            sha256 = calculate_sha256(original_filepath)

            name_part, ext_part = os.path.splitext(filename)
            new_filename = f"{name_part}_{sha256}{ext_part}"
            output_filepath = os.path.join(output_dir, new_filename)

            shutil.copy2(original_filepath, output_filepath)
            print(f"已复制: {filename} -> {new_filename}")

    print("所有 .map 文件处理完成！")

if __name__ == "__main__":
    main()