---
marp: true
---

- Specification
```
READ|WRITE

SLI: Availability (ErrorRate per 5min) = number of reqs with status != 5xx / number of all reqs * 100
SLO 95%, 5m

SLI: Latency per 5min                 = number of reqs from 1s bucket/ number of all reqs * 100
SLO 99%, 1s, 5m

SLI: Throughput                       = number of requests / time window
SLO 1000 reqs/min

```
---
- Realization
```
Source : server prometheus logs

GET|POST

Availability

(request_total:rate5m{verb="read",code!~"5.."} / request_total:rate5m{verb="read"}) * 100
(request_total:rate5m{verb="write",code!~"5.."} / request_total:rate5m{verb="write"}) * 100

Latency

(sum(rate(request_time_bucket{le="1s",verb="read"}[5m])) / sum(rate(request_time_count[5m]))) * 100
(sum(rate(request_time_bucket{le="1s",verb="write"}[5m])) / sum(rate(request_time_count[5m]))) * 100

Throughput

request_total:rate1m{verb="read"}
request_total:rate1m{verb="write"}

```
---
- Uncovered cases

```
Requests to old_domain.com
```