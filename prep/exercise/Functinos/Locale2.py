def extract_region(code):
  return code[3:5]

print(extract_region('en_US.UTF-8'))      # en
print(extract_region('en_GB.UTF-8'))      # en
print(extract_region('ko_KR.UTF-16'))     # ko