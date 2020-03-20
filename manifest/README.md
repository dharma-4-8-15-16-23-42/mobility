# Kubernetes Deployment Files

Deployment manifests for the mobility microservice.

## Usage

The service's version information will be exposed via a global `api-ingress` at the address:

```
http://<INGRESS IP>/mobility/version
```

## Rolling Update Deployment

To set up a mobility deployment, and ingress, configured with a rolling update deployment strategy:

```console
foo@bar:~$ kubectl apply -f rolling-update-deployment.yaml
```

To perform a rolling update from version `v0.0.1` to `v0.0.2`:

```console
foo@bar:~$ kubectl set image deployment/mobility-deployment mobility=dharma4815162342/mobility:v0.0.2 --record
```

## Blue Green Deployment

To set up a mobility deployment, and ingress, configured with a blue green deployment strategy:

```console
foo@bar:~$ kubectl apply -f blue-green-deployment.yaml
```

### Perform Deployment

To perform a blue green deployment:

1. Deploy a new version for testing:

```console
foo@bar:~$ kubectl apply -f blue-green-update.yaml
foo@bar:~$ kubectl patch service mobility-testing -p '{"spec":{"selector":{"version": "v0.0.2"}}}'
```

2. Perform any prerelease checks by testing against: `http://mobility-testing.default.svc`.

3. Switch over production traffic via:

```console
foo@bar:~$ kubectl patch service mobility -p '{"spec":{"selector":{"version": "v0.0.2"}}}'
```

4. Cleanup the old deployment once all traffic has drained.

```console
foo@bar:~$ kubectl delete deployment mobility-deployment-v0.0.1
```
