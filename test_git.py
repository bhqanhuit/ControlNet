from onedrivedownloader import download


url = "curl -I https://davian-lab.tw4.quickconnect.to/d/s/p9A5kbK4danKU4WeoqSMiudPFX7Qmiau/webapi/entry.cgi/SYNO.SynologyDrive.Files/images_mqset001.zip?api=SYNO.SynologyDrive.Files&method=download&version=2&download_type=%22download%22&files=%5B%22id%3A692403417502495374%22%5D&force_download=true&json_error=true&_dc=1715245037491&sharing_token=%22ZcSiSiVuJpSW_3qeEF97XYtExUQqKeb1p8H2Lbr.32iSJ2.DyHNxNkLV46rSLT9fvzKl4gMZ1xj4Pdfn5HBnr20Q60ngATR7teJ1lIXkFfkMvGXNHYTIxdBdPt2w39DEHRN9oTk58_DD0AoVLvXak2G0SVyhmkSMdVnkQXyUp0ZPy6l572oCl3MTCnCdsm1B86wBWbDlyslk5EK3YLDPNISWWZikMRwl_yId2VMNB5Y14OMB8xZIuWYB%22"
download(url, filename="something.zip", unzip=True, unzip_path="./data")

