# k8s安装说明
## 1. 2台主机都要安装docker
## 2. 2台主机都要安装kubeadm,kubelet和kubecrl
## 3. 2台主机都要禁用虚拟内存
   > #####  swapoff -a

### （一）安装kubeadm,kubelet和kubecrl
#### 1. apt-get update && apt-get install -y apt-transport-https curl
#### 2. curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add-cat <<EOF>/etc/apt/sources.list.d/kubernetes.listdeb http://apt.kubernetes.io/ kubernetes-xenial main EOF
#### 3. apt-get update && apt-get install -y kubelet kubeadm kubectl
####