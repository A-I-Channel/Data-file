
cd /content
!pip install pycloudflared
!pip install insightface==0.7.3
pip install onnx==1.14.0
pip install onnxruntime==1.15.0
pip install opencv-python==4.7.0.72
pip install tqdm
sde = "stable"
sdq= "-diffusion-webui"
sdw = sde+sdq
sda = "AUTOMATIC1111"
dest = "sd-webui-controlnet"
webs = sdw+"-images-browser"
sd = "sd-webui"
cut1 = "-cutoff"
regin1 = "-regional-prompter"
regin = sd+regin1
cutoof = sd+cut1
tunk = "-tunnels"
rops = "-roop"
swaprop = sd+rops
tunell = sd+tunk
%cd /content
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui