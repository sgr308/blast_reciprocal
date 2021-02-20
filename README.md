# blast_reciprocal

The "blast_reciprocal.py" script developed in python to get reciprocal hits between two species based on blast results.

The script was tested on "blastp" program using blast 2.3.0 version.

# STEPS:
```bash
blastp -subject species1.fa -query species2.fa -outfmt 6 -out blastresults_1.txt -num_threads 15 -max_target_seqs 1
```
- Change query and sequence data and again do blastp:
```bash
blastp -subject species2.fa  -query species1.fa -outfmt 6 -out blastresults_2.txt -num_threads 15 -max_target_seqs 1
```
- Now, use "blast_reciprocal.py" python script to get reciprocal hits from these above two blastp results. Edit the filepath names in "blast_reciprocal.py" before running it.
