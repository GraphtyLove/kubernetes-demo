# kubernetes-demo

Small Demo to show how to deploy on Kubernetes

## API

The API is a simple FastAPI application.

### Build & push the image

Create an account on [Docker Hub](hub.docker.com/).

```bash
# Login to Docker Hub
docker login
# Build the image
docker build -t <your-docker-hub-username>/api-demo:latest .
# Push the image
docker push inoopa/api-demo:latest
```

If you are on a Mac with M1, M2, M3,... you can use the following command to build & push the image:

*[More information](https://stackoverflow.com/questions/74942945/how-to-build-a-docker-image-for-m1-mac-silicon-or-amd-conditionally-from-dockerf)*

```bash
docker buildx build --platform linux/amd64 --push -t <your-docker-hub-username>/api-demo:latest .
```

### Run locally

```bash
docker run -p 80:80 <your-docker-hub-username>/api-demo:latest
```

## Kubernetes

The Kubernetes manifests are in the `kubernetes` folder.

```bash
kubectl apply -f kubernetes/manifest.yaml
```

Then you need to forward the port to your local machine:

```bash
kubectl port-forward -n api-demo-namespace service/api-demo-service 8080:80
```
