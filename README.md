# Demo_Kafka_Confluent for Learning 
this this example or template for studying about Kafka that setup on docker environment and if you need more information about this please following this before: https://developer.confluent.io/get-started/python/

let's go!   

### Pre-request
- WSL (Windows Sub-system Linux)
- Docker 

## Entiring project environment
This project uses the following environment variables on linux, so we can use the linux conmand-line for testing anything in our project. 

activate environment use: 

``` sources env/bin/activate ```

deactivate environment use:

``` deactivate env/bin/deactivate```


## Running Kafka container 

comand-line for running Kafka containers:


``` docker-compose up -d ```

## Create Topic
Events in Kafka are organized and durably stored in named topics. Topics have parameters that determine the performance and durability guarantees of the events that flow through them.
Create a new topic, purchases, which we will use to produce and consume events.

We'll use the kafka-topics command located inside the local running Kafka broker:


```
docker compose exec broker kafka-topics --create --topic purchases --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1  
```

And we will use the this command-line to show list of topics in kafka:

```
docker exec <kafka-container-name> kafka-topics --list --bootstrap-server localhost:9092
```

## Produce Events

run on command-line``` python run producer.py``` on virtualenv, and don't forget to cd directly to each a Lab directly on repository.


## Consume Events

run on command-line``` python run Consumer.py``` on virtualenv, and don't forget to cd directly to each a Lab directly on repository.


Note that should be start with Lab_2 and Lab_3 
so, exercise is run any thing in directorie on Lab_1 at last. 

Good luck! 



