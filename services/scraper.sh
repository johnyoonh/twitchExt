#!/bin/bash
echo getting A

Curl -H "accept: application/json" 'http://api.7digital.com/1.2/artist/browse?shopId=2020&oauth_consumer_key=7d4vr6cgb392&letter=a&pagesize=50&page=1' >> artists.json

echo getting A pt 2

Curl -H "accept: application/json" 'http://api.7digital.com/1.2/artist/browse?shopId=2020&oauth_consumer_key=7d4vr6cgb392&letter=a&pagesize=50&page=2' >> artists.json

echo getting A pt 3

Curl -H "accept: application/json" 'http://api.7digital.com/1.2/artist/browse?shopId=2020&oauth_consumer_key=7d4vr6cgb392&letter=a&pagesize=50&page=3' >> artists.json