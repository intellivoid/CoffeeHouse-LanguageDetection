import os
from setuptools import setup, find_packages

# Find all the stopwords data files
data_file_path = os.path.join('coffeehouse_languagedetection', 'data')

data_files_fetch = os.listdir(os.path.join(os.getcwd(), data_file_path))
data_files = []
for file in data_files_fetch:
    file_path = os.path.join(os.getcwd(), data_file_path, file)
    if not os.path.isdir(file_path):
        data_files.append(file_path)


model_file_path = os.path.join('coffeehouse_languagedetection', 'data', 'langdetect_build')

model_files_fetch = os.listdir(os.path.join(os.getcwd(), model_file_path))
model_files = []
for file in model_files_fetch:
    file_path = os.path.join(os.getcwd(), model_file_path, file)
    if not os.path.isdir(file_path):
        model_files.append(file_path)


profiles_file_path = os.path.join('coffeehouse_languagedetection', 'data', 'profiles')

profiles_files_fetch = os.listdir(os.path.join(os.getcwd(), profiles_file_path))
profiles_files = []
for file in profiles_files_fetch:
    file_path = os.path.join(os.getcwd(), profiles_file_path, file)
    if not os.path.isdir(file_path):
        profiles_files.append(file_path)

setup(
    name='coffeehouse_languagedetection',
    version='1.0.0',
    description='Multi-method Language Detection Library',
    url='https://github.com/Intellivoid/CoffeeHouse-LanguageDetection',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Text Processing',
        'Programming Language :: Python :: 3',
    ],
    keywords='machine learning language detection',
    data_files=[
        (os.path.join('coffeehouse_languagedetection', 'data'), data_files),
        (os.path.join('coffeehouse_languagedetection', 'data', 'langdetect_build'), model_files),
        (os.path.join('coffeehouse_languagedetection', 'data', 'profiles'), profiles_files),
        (
            os.path.join('coffeehouse_languagedetection', 'ldutils'),
            [os.path.join(os.getcwd(), 'coffeehouse_languagedetection', 'ldutils', 'messages.properties')]
        )
    ],
    install_requires=[
        'scikit-learn==0.22.0',
        'joblib',
        'six'
    ],
    packages=find_packages()
)
