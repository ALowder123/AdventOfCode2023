use std::fs::File;
use std::io::{BufRead, BufReader};

fn check_north(r: usize, c: usize, p: &Vec<Vec<char>>) -> bool{
    let north = p[r-1][c];
    match north {
        '|' | '7' | 'F' =>  return true,
        _ => return false
    };
}
fn check_south(r: usize, c: usize, p: &Vec<Vec<char>>) -> bool{
    let south = p[r+1][c];
    match south {
        '|' | 'L' | 'J' => return true,
        _ => return false
    };
}
fn check_east(r: usize, c: usize, p: &Vec<Vec<char>>) -> bool{
    let east = p[r][c+1];
    match east {
        '-' | 'J' | '7' => return true,
        _ => return false
    };
}
fn check_west(r: usize, c: usize, p: &Vec<Vec<char>>) -> bool{
    let west = p[r][c-1];
    match west {
        '-' | 'L' | 'F' => return true,
        _ => return false
    };
}


fn find_pipe(r: usize, c: usize, p: &Vec<Vec<char>>, ch: char, dir: char) -> (usize, usize, char){
    //check north
    if ch == '|' || ch == 'L' || ch == 'J' {
        if dir != 'n' && check_north(r, c, p) {
            return (r-1, c, 's');
        }
    }
    // check east
    if ch == '-' || ch == 'L' || ch == 'F' {
        if dir != 'e' && check_east(r, c, p) {
            return (r, c+1, 'w');
        }
    }
    // check south
    if ch == '|' || ch == '7' || ch == 'F' {
        if dir != 's' && check_south(r, c, p) {
            return (r+1, c, 'n');
        }
    }
    // check west
    if ch == '-' || ch == 'J' || ch == '7' {
        if dir != 'w' && check_west(r, c, p){
            return (r, c-1, 'e');
        }
    }
    
    return (r, c, dir);
    
}

fn find_start_pipes(r: usize, c: usize, p: &Vec<Vec<char>>) -> (usize, usize, usize, usize){
    let mut p0 = 0;
    let mut p1 = 0;
    let mut p2 = 0;
    let mut p3 = 0;
    if check_north(r, c, p) {
        p0 = r-1;
        p1 = c;
    }
    if check_east(r, c, p) {
        if p0 == 0 {
            p0 = r;
            p1 = c+1;
        }
        else {
            p2 = r;
            p3 = c+1;
        }
    }
    if check_south(r, c, p) {
        if p0 == 0 {
            p0 = r+1;
            p1 = c;
        }
        else {
            p2 = r+1;
            p3 = c;
        }
    }
    if check_west(r, c, p) {
        p2 = r;
        p3 = c-1;
    }

    return (p0, p1, p2, p3);


}

fn main() -> Result<(), std::io::Error> {
    let file: File = File::open("./pipes.txt")?;
    let reader: BufReader<File> = BufReader::new(file);
    let mut pipe = vec![vec![]];
    let (mut s_row, mut s_col): (usize, usize) = (0, 0);
    pipe.remove(0);
    //put pipe in 2d vec and find index of S
    for line in reader.lines() {
        let y = line.unwrap();
        if y.contains("S") {
            s_row = pipe.len();
            s_col = y.find("S").unwrap();
        }
        pipe.push(y.chars().collect());
    }
    // get the locations of the two pipes connected to S
    let (mut p1_dir, mut p2_dir) : (char, char) = ('a', 'a');
    let (mut p1_row, mut p1_col, mut p2_row, mut p2_col) = find_start_pipes(s_row, s_col, &pipe);

    // go from both ends and meet at the middle finding the farthest pipe
    let mut distance = 1;
    while p1_row != p2_row || p1_col != p2_col {
        (p1_row, p1_col, p1_dir) = find_pipe(p1_row, p1_col, &pipe, pipe[p1_row][p1_col], p1_dir);
        (p2_row, p2_col, p2_dir) = find_pipe(p2_row, p2_col, &pipe, pipe[p2_row][p2_col], p2_dir);
        distance += 1;
    }
    println!("{}", distance);

    Ok(())
}
