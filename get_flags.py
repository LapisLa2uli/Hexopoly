import pycountry
import os
import requests
'''
# Directory to save the flags
output_dir = "country_flags"
os.makedirs(output_dir, exist_ok=True)

# Base URL for flagcdn.com (JPGs via alpha-2 codes)
base_url = "https://flagcdn.com/w320/{code}.jpg"

for country in pycountry.countries:
    try:
        alpha_2 = country.alpha_2.lower()
        country_name = country.name
        flag_url = base_url.format(code=alpha_2)
        response = requests.get(flag_url)

        if response.status_code == 200:
            file_path = os.path.join(output_dir, f"{country_name}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Saved flag for {country_name}")
        else:
            print(f"Failed to download flag for {country_name} ({alpha_2})")

    except Exception as e:
        print(f"Error processing {country.name}: {e}")
'''
with open('countries.txt')as f:
    txt=f.readlines()
txt=list(map(lambda x:x.split(', '),txt))
for y in range(len(txt)):
    for x in range(len(txt[y])):
        txt[y][x]=txt[y][x].strip('\n')
import os
os.chdir('country_flags')
print(txt)
for flag in os.listdir('.'):
    mark=1
    print(flag)
    if any(char.isdigit() for char in flag):
        continue
    for y in range(len(txt)):
        for x in range(len(txt[0])):
            if txt[y][x].lower() in flag.replace('_',' ').lower():
                try:
                    os.rename(flag, f'{y}{chr(x + 97)}.jpg')
                except FileExistsError:
                    continue
                mark=0
                break
        if mark==0:
            break
    if mark==1:
        print('ERROR: ',flag)