# lab

## Arista (GNMI/SNMP/EAPI) Telegraf + Prometheus + Grafana

### Intro

Stream Telemtry from Arista EOS devices via Telegraf/GNMI to Prometheus and visualized with Grafana.

### Reference Material

- [arista-netdevops-community/automation_and_telemetry_demo](https://github.com/arista-netdevops-community/automation_and_telemetry_demo)
- [Introduction to a Telemetry Stack - Part 1](https://blog.networktocode.com/post/telemetry-stack-series-part-01/)
- [Introduction to a Telemetry Stack - Part 2](https://blog.networktocode.com/post/telemetry-stack-series-part-02/)
- [Introduction to a Telemetry Stack - Part 3](https://blog.networktocode.com/post/telemetry-stack-series-part-03/)
- [Introduction to a Telemetry Stack - Part 4](https://blog.networktocode.com/post/telemetry-stack-series-part-04/)
- [Monitor Your Network With gNMI, SNMP, and Grafana](https://blog.networktocode.com/post/monitor_your_network_with_gnmi_snmp_and_grafana/)
- [Open Source Network Management](https://leanpub.com/opensourcenetworkmanagement)

### Getting Started

1. Install [ContainerLab](https://containerlab.dev/)

2. Start the Lab

```bash
sudo containerlab deploy -t clab.yml
```

3. Browse to the relevant tool

- [Grafana](http://localhost:3000/) admin:admin
- [Telegraf](http://localhost:9011/metrics)
- [Prometheus](http://localhost:9090/)

### Current Status

- [x] Arista cEOS
  - [x] SNMP
  - [x] gNMI
  - [x] EAPI
- [x] Telegraf
- [x] Prometheus
- [] Grafana Dashboards (All examples use influxdb, need to conver queries)
- [] NetBox data enrichment

## Arista (GNMI) Telegraf + Kafka + python writer to Postgres - Route table tracking

### Intro

Stream Telemtry for non TSDB data like route tables from Arista EOS devices via Telegraf/GNMI OR GNMIC to Kafka to a python process to a datbase.

### Reference Material

### Getting Started

1. Install Docker & Docker-Compose

2. Start the Lab

```bash
docker-compose up -d
```

3. Browse to the relevant tool

- [NetBox](http://localhost:8000/) admin:admin

### Current Status

- [x] Arista cEOS
  - [x] SNMP
  - [x] gNMI
  - [x] EAPI
- [] Telegraf / GNMIC
- [] Kafka
- [] Kafka-UI
- [] Postgres
- [] Redash
- [] NetBox data enrichment

### Day 1 Tables

- routes
- history_routes
