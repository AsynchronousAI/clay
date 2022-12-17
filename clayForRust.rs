use std::fs;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::path::Path;

use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct Runlogs {
    requests: Vec<String>,
    data: Vec<String>,
    r#return: Vec<String>,
}

fn reply(value: String) {
    let mut data: Runlogs = read_json("Runlogs.json").unwrap();
    data.r#return.push(value);
    write_json("Runlogs.json", data).unwrap();
}

fn send(name: String, dt: String) {
    let mut data: Runlogs = read_json("Runlogs.json").unwrap();
    data.requests.push(name);
    data.data.push(dt);
    write_json("Runlogs.json", data).unwrap();
}

fn recieve() -> String {
    let mut data: Runlogs = read_json("Runlogs.json").unwrap();
    let value: String = data.data.pop().unwrap();
    write_json("Runlogs.json", data).unwrap();
    value
}

fn read_json<T>(path: &str) -> Result<T, serde_json::Error>
where
    T: for<'de> Deserialize<'de>,
{
    let file = File::open(path)?;
    let buf_reader = BufReader::new(file);
    let data: T = serde_json::from_reader(buf_reader)?;

    Ok(data)
}

fn write_json<T>(path: &str, data: T) -> Result<(), serde_json::Error>
where
    T: Serialize,
{
    let json = serde_json::to_string(&data)?;
    let path = Path::new(path);
    let display = path.display();

    let mut file = match File::create(path) {
        Err(why) => panic!("couldn't create {}: {}", display, why),
        Ok(file) => file,
    };

    match file.write_all(json.as_bytes()) {
        Err(why) => panic!("couldn't write to {}: {}", display, why),
        Ok(_) => println!("successfully wrote to {}", display),
    }

    Ok(())
}