# K8S

## Manual deployment

### Create deployment and service

![img.png](images/img1.png)

### Application test after created deployment and service

![images/img.png](images/img2.png)

### Status

![images/img.png](images/img3.png)

**External-ip is still pending, but it will be there in some time.**  
I've noticed than it would be **192.168.49.2**, because of the minikube tunnel configuration.  
Route: 10.96.0.0/12 -> 192.168.49.2, machineName: minikube, Pid: 45246

### Clean up

![images/img.png](images/img4.png)

## Deployment with configuration

### Create deployment and service using manifest

![img.png](images/img5.png)

### Status

![img.png](images/img6.png)

Let's check:

![img.png](images/img8.png)

![img.png](images/img7.png)

## Helm

### Installation

```bash
helm install devops-web-app-chart ./devops-web-app-chart
```

### Status

![img.png](images/img9.png)

![img.png](images/img10.png)

![img.png](images/img11.png)

![img.png](images/img12.png)
