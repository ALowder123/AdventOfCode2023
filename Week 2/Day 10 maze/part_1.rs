use std::fs::File;
use std::io::{BufRead, BufReader};

fn all_same(v: &Vec<i32>) -> bool {
    for i in 0..v.len()-1 {
        if v[i] != v[i+1] {
            return false;
        }
    }
    return true;
}

fn sequences(v: Vec<i32>) -> i32{
    let mut sequence = vec![vec![]];
    for x in v {
        sequence[0].push(x);
    }
    let mut cur = 0;
    while !all_same(&sequence[cur]) {
        sequence.push(Vec::new());
        for i in 0..sequence[cur].len()-1 {
            let x = sequence[cur][i+1] - sequence[cur][i];
            sequence[cur+1].push(x);
        }
        cur += 1;
    }
    for x in (1..cur+1).rev() {
        let y = sequence[x][sequence[x].len()-1] + sequence[x-1][sequence[x-1].len()-1];
        sequence[x-1].push(y);
    }

    return sequence[0][sequence[0].len()-1];
}


fn main() -> Result<(), std::io::Error> {
    let file: File = File::open("./mirage.txt")?;
    let reader: BufReader<File> = BufReader::new(file);
    let mut res = 0;

    for line in reader.lines(){
        let vals: Vec<i32> = line.unwrap().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
        res += sequences(vals);
    }

    println!("{}", res);

    Ok(())
}
