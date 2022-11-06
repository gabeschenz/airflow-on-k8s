This repo is the configuration I have used in a Medium article.  Here is the copy pasta, if that's how you roll:

```
set -e
/bin/bash -c $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)
brew install k3d helm kubernetes-cli watch
CLUSTER_NAME="airflow-on-k8s"
k3d cluster create "${CLUSTER_NAME}" \
        --registry-create "${CLUSTER_NAME}-registry:0.0.0.0:5000"
helm repo add apache-airflow https://airflow.apache.org
ssh-keygen -t ed25519 -N '' -f airflow-deploy-key
base64_encrypted_private_key="$(cat airflow-deploy-key | base64)"
sed -i -e "s/LS0.../${base64_encrypted_private_key}/" git-sync-secret.yaml
sed -i -e "s#git@github.com:gabeschenz/airflow-on-k8s.git#git remote get-url origin#" values.yaml
kubectl apply -f git-sync-secret.yaml

read -s "?Now you need to add the public key to your github repo's deploy keys.  Hit enter when that's complete."
helm upgrade airflow apache-airflow/airflow --debug -f ./values.yaml
kubectl port-forward svc/airflow-webserver 8080:8080
```
