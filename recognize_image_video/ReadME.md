pip - пакетный менеджер (https://pypi.org/)
homebrew (https://brew.sh/) - пакетный менеджер для MacOs/Linux

Распознавание объектов на Python / Глубокое машинное обучение

-----------------------------------------------------------------------------------------------------------
1. Download Anaconda - https://www.anaconda.com/distribution/#download-section
2. Create environment - conda create --name tetgun python=3.7
3. Open - Anaconda PowerShell
start - C:\Users\y.buhera\AppData\Local\Continuum\anaconda3\etc\profile.d\conda.sh
conda init

4. Restart shell
5. conda activate tetgun_active ------OR------ CALL conda.bat activate tetgun_active
Install torch module for tetgun project
6. conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

Env name - tetgun

Download modules - pip install module_name

python test.py --style_name ../data/style/26.jpg --content_name ../data/content/2.png --name my26_2.png
-----------------------------------------------------------------------------------------------------------
conda info --env - просмотр созданных окружений

Steps:
1. Install anaconda(conda) with version of python 3.6
2. Execute all steps for creating environments
3. Install packages
4. https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection - url for download Retina Net model
5. https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/ - url for download model for video


