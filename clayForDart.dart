import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'dart:typed_data';

class NoneToEmptyJSON extends JsonEncoder {
  const NoneToEmptyJSON() : super.withIndent('  ');

  @override
  Object convert(Object object) {
    if (object == null) {
      object = '';
    } else if (object is Map) {
      return {convert(key): convert(value) for key, value in object.items()};
    } else if (object is List || object is Tuple) {
      return [convert(item) for item in object];
    }
    return object;
  }

  @override
  String convert(Object object) {
    return super.convert(convert(object));
  }
}

void reply(value) {
  var data = [];
  var file = File("Runlogs.json");
  var text = file.readAsStringSync();
  data = json.decode(text);
  file.close();
  data["return"].add(value);
  file = File("Runlogs.json");
  if (data != null) {
    file.writeAsStringSync(NoneToEmptyJSON().convert(data));
    file.close();
  }
}

void send(name, dt = "None") {
  // Read Runlogs.json
  var data = [];
  var file = File("Runlogs.json");
  var text = file.readAsStringSync();
  data = json.decode(text);

  // Append name to data.requests
  data["requests"].add(name);
  data["data"].add(dt);

  // Write data to Runlogs.json
  file = File("Runlogs.json");
  file.writeAsStringSync(json.encode(data));
}

Object recieve() {
  // return the last value in Runlogs.json and remove it
  var data = [];
  var file = File("Runlogs.json");
  var text = file.readAsStringSync();
  data = json.decode(text);
  file.close();

  var value = data["data"][-1];
  return value;
}