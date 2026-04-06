use std::{fs, io::Write};

fn main() {
	let mut file_w = fs::File::create("./data.json").unwrap();
	file_w.write_all(b"[\n{\"time\": \"get_time_here\"}\n]").unwrap();
}
