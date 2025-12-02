use std::fs;

fn main() {
    let mut out = String::new();

    // iterate over entries like 2024/, 2025/
    for entry in fs::read_dir(".").unwrap() {
        let path = entry.unwrap().path();
        if !path.is_dir() {
            continue;
        }

        // year folder = directory with a numeric name
        let year = path.file_name().unwrap().to_string_lossy();
        if !year.chars().all(|c| c.is_ascii_digit()) {
            continue;
        }

        // push: pub mod y2024 { ... }
        out.push_str(&format!("pub mod _{year} {{\n"));

        // find all .rs files in the year folder
        for file in fs::read_dir(&path).unwrap() {
            let file = file.unwrap().path();
            if file.extension().and_then(|s| s.to_str()) == Some("rs") {
                let name = file.file_stem().unwrap().to_string_lossy();
                out.push_str(&format!("    #[path = \"../../{year}/{name}.rs\"]\n"));
                out.push_str(&format!("    pub mod {name};\n"));
            }
        }

        out.push_str("}\n\n");
    }

    fs::write("src/generated_years.rs", out).unwrap();

    // Re-run script if year folders change
    println!("cargo:rerun-if-changed=.");
}
