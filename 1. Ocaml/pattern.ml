let print_spaces num_spaces =
  for _ = 1 to num_spaces do
    print_string " ";
  done

let print_stars num_stars =
  for _ = 1 to num_stars do
    print_string "*";
  done

let print_diamond_pattern height =
  let max_width = height * 2 - 1 in
  for row = 1 to height do
    let num_spaces = abs (height - row) in
    let num_stars = max_width - (2 * num_spaces) in
    print_spaces num_spaces;
    print_stars num_stars;
    print_newline ();
  done

let () =
  print_string "Enter the height of the diamond: ";
  flush stdout;
  let height = read_int () in
  if height mod 2 = 0 then
    Printf.printf "Please enter an odd height for a symmetric diamond.\n"
  else
    print_diamond_pattern height
