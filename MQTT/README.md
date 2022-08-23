# MQTT Notes

## Public MQTT Brokers
### mqtt.eclipseprojects.io
* 1883 : MQTT over unencrypted TCP
* 8883 : MQTT over encrypted TCP
* 80   : MQTT over unencrypted WebSockets (note: URL must be /mqtt )
* 443  : MQTT over encrypted WebSockets (note: URL must be /mqtt )

### test.mosquitto.org
* 1883 : MQTT, unencrypted, unauthenticated
* 1884 : MQTT, unencrypted, authenticated
* 8883 : MQTT, encrypted, unauthenticated
* 8884 : MQTT, encrypted, client certificate required
* 8885 : MQTT, encrypted, authenticated
* 8886 : MQTT, encrypted, unauthenticated
* 8887 : MQTT, encrypted, server certificate deliberately expired
* 8080 : MQTT over WebSockets, unencrypted, unauthenticated
* 8081 : MQTT over WebSockets, encrypted, unauthenticated
* 8090 : MQTT over WebSockets, unencrypted, authenticated
* 8091 : MQTT over WebSockets, encrypted, authenticated