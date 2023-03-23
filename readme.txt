Command list from start :

installing pip3

  sudo apt-get install python3-pip
  
  
Following https://forums.developer.nvidia.com/t/object-detection-with-jetson-nano/198189/9

1. Prerequisites (done)
  sudo apt-get install gfortran libopenblas-dev liblapack-dev                                         (done)
  sudo pip3 install scikit-build                                                                      (done)
  
2. Cloning the repo
  git clone https://github.com/NVIDIA-AI-IOT/scene-text-recognition.git                               (done)
  cd scene-text-recognition/
  git submodule update --init --recursive                                                             (done)
  
  
  mv {scene.patch} .                                                                                  (done)
  git apply scene.patch                                                                               (done)
  
  cd EasyOCR/
  mv {easyocr.patch} .
  git apply easyocr.patch
  
3. Install pytorch, torchvision
  wget https://raw.githubusercontent.com/tomek-l/jetson-install-pytorch/master/install_torch_v1.9.sh  (done)
  sed -i 's/# install_torch/install_torch/g' install_torch_v1.9.sh                                    (done)
  bash install_torch_v1.9.sh                                                                          (done)
  pip3 install -r requirements.txt                                                                    (done)    
  
4. Install torch2trt
  cd torch2trt                                                                                        (done)          
  sudo python3 setup.py install --plugins                                                             (done)
  cd ..                                                                                               (done)

5. Install EasyOCR
  cd EasyOCR
  sudo python3 setup.py install

6. Testing
  python3 easy_ocr_demo.py /home/nvidia/scene-text-recognition/docs/images/
