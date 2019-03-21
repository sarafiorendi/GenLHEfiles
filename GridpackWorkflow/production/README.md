# Gridpack production

- Select a model, e.g. SMS-StopStop, and modify the templatecards
- Use a modification of `writeallcards_SMS-StopStop.sh` to create the cards for the various jobs
- Use a modification of `submitallgridpackjobs_SMS-StopStop.sh` to submit the jobs to condor. Attention: On lxplus, paths should be absolute!
- Gridpacks and logs should appear in the directory from which you submitted.
- If single jobs fail they can be resubmitted using `condor_submit MYCONDORSUBMITFILE.cmd`, where the condor submit file is automatically created when submitting the jobs for the first time.
