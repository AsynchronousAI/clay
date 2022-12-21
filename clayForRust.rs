pub fn send(file: &str, data: &str) {
    // Read Runlogs.json file
    let mut file = File::open("Runlogs.json").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();

    // Convert to JSON
    let mut json: Value = serde_json::from_str(&contents).unwrap();

    // Append file variable to JSON.requests
    json["requests"].as_array_mut().unwrap().push(json!(file));

    // Append data variable to JSON.data
    json["data"].as_array_mut().unwrap().push(json!(data));

    // Convert back to string
    let json = json.to_string();

    // Write to Runlogs.json file
    let mut file = File::create("Runlogs.json").unwrap();
}

pub fn reply(data: &str) {
    // Read Runlogs.json file
    let mut file = File::open("Runlogs.json").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();

    // Convert to JSON
    let mut json: Value = serde_json::from_str(&contents).unwrap();

    // Append data variable to JSON.return
    json["retrun"].as_array_mut().unwrap().push(json!(data));

    // Convert back to string
    let json = json.to_string();

    // Write to Runlogs.json file
    let mut file = File::create("Runlogs.json").unwrap();
}

pub fn request(){
    // Return newest value in JSON.data

    // Read Runlogs.json file
    let mut file = File::open("Runlogs.json").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();

    // Convert to JSON
    let mut json: Value = serde_json::from_str(&contents).unwrap();

    // Get newest value in JSON.data
    let data = json["data"].as_array_mut().unwrap().pop().unwrap();

    // Convert back to string
    let data = data.to_string();

    // Return data
    return data;
}