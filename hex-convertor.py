import struct

def convert_little_to_big_endian(input_file_path, output_file_path):
    # Read the little-endian data from the input file
    with open(input_file_path, 'rb') as input_file:
        little_endian_data = input_file.read()
    
    num_elements = len(little_endian_data) // 4
    big_endian_data = bytearray()

    # Slicing every 4 bytes together
    for i in range(num_elements):
        little_endian_chunk = little_endian_data[i*4:(i+1)*4]
        value = struct.unpack('<I', little_endian_chunk)[0]  # Little-endian unpacking
        big_endian_chunk = struct.pack('>I', value)  # Converting to big-endian
        big_endian_data.extend(big_endian_chunk)
    
    # Writing the big-endian data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(big_endian_data)
    
    print(f"Conversion complete. Output saved to {output_file_path}")


input_file_path = "./challengefile.jpg"
output_file_path = "./challengefinal.jpg"

convert_little_to_big_endian(input_file_path, output_file_path)
