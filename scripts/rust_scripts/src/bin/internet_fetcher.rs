use std::{fs::{self, OpenOptions}, io::{Bytes, Seek, Write}, os::unix::fs::FileExt};
use std::io::SeekFrom;

use scraper::{Html, Selector, element_ref};
use tokio::io::split;

fn main() {
	let file_html = fs::read_to_string("./index.html").unwrap();
	let data_document = Html::parse_document(&file_html);
	let fetchable_divs = Selector::parse(".panel-heading").unwrap();
	let file_w = OpenOptions::new()
		.write(true)
		.truncate(false)
		.create(true)
		.open("./data.json").unwrap();
	let mut file_input_str = String::new();
	print!("{file_html}");
	file_w.write_all_at(b",{{\"time\": \"get_time_here\"}\n", file_w.metadata().unwrap().len()-1).unwrap();
	for element in data_document.select(&fetchable_divs) {
		let element_full = element.text().collect::<String>();
		let mut split_element:Vec<&str> = element_full.split(' ').collect();
		let element_name = split_element[split_element.len()-1];
		split_element.pop();
		if(element_name == ""){
			continue;
		}
		let mut element_value = String::new();
		for items in split_element {
		  element_value = format!("{element_value}{items}");
		}
		//let element_value = split_element.collect::<String>();
		file_input_str = format!(",{{\"{element_name}\": \"{element_value}\"}}\n");
		file_w.write_all_at(file_input_str.as_bytes(), file_w.metadata().unwrap().len()).unwrap();
	}
	file_w.write_all_at(b"}]", file_w.metadata().unwrap().len()).unwrap();
}
