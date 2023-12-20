use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

fn getmap(line: String,  dir: &mut HashMap<String, Vec<String>>){
    let mut items: Vec<String> = vec![];
    let mut key: String = " ".to_string();
    for v in line.split(' ') {
        if v.contains("=") {
            continue;
        } 
        else if v.contains("(") { //first value
            items.push(String::from_utf8(v.as_bytes()[1..4].to_ascii_uppercase()).unwrap());
        }
        else if v.contains(")") { //second value
            items.push(String::from_utf8(v.as_bytes()[0..3].to_ascii_uppercase()).unwrap());
        }
        else {
            key = v.to_string(); //key value
        }  
    }
    if items.len() == 0 {
        return;
    }
    dir.insert(key, items);

}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("./directions.txt")?;
    let reader = BufReader::new(file);
    let mut order: Vec<char> = vec![];
    let mut dir: HashMap<String, Vec<String>> = HashMap::new();
    // Get the order of directions and map all of the direction values
    for line in reader.lines() {
        if order.len() == 0{
            order = line?.chars().collect();
        }
        else{
            getmap(line?.to_string(), &mut dir);
        }
    }
    let mut key = "AAA".to_string();
    let mut steps = 0;
    while key != "ZZZ".to_string(){
            for x in &order{
            let value = dir.get(&key).unwrap();
            if x == &'L'{
                key = value[0].to_string();
            }
            else {
                key = value[1].to_string();
            }
            steps += 1;
        }
    }
    
    println!("Steps = {}", steps);
    Ok(())
}
