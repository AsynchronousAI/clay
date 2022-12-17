#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
void reply(std::string value){
    json data;
    std::ifstream file("Runlogs.json");
    file >> data;
    data["return"].push_back(value);
    std::ofstream file2("Runlogs.json");
    file2 << data;
}
void send(std::string name, std::string dt = "None"){
    // Read Runlogs.json
    json data;
    std::ifstream file("Runlogs.json");
    file >> data;
    // Append name to data.requests
    data["requests"].push_back(name);
    data["data"].push_back(dt);
    // Write data to Runlogs.json
    std::ofstream file2("Runlogs.json");
    file2 << data;
}
std::string recieve(){
    // return the last value in Runlogs.json and remove it
    json data;
    std::ifstream file("Runlogs.json");
    file >> data;
    return data["data"].back();
}