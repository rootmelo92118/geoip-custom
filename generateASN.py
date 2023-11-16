import csv, sys

def main(csv_path=["GeoLite2-ASN-Blocks-IPv4.csv", "GeoLite2-ASN-Blocks-IPv6.csv"], output="./"):
    asnlist = []
    asndict = {}
    print("Start to Read data...")
    for csvpath in csv_path:
        with open(csvpath, newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                if row['autonomous_system_number'] not in asnlist:
                    asndict[row['autonomous_system_number']] = [row['network']]
                    asnlist.append(row['autonomous_system_number'])
                    print("Found a new AS Number : AS" + row['autonomous_system_number'])
                else:
                    asndict[row['autonomous_system_number']].append(row['network'])
            csvfile.close()
    print("Data read finished ! \nGenerate plain text file...")
    for i in asnlist:
        exportData = ""
        for j in asndict[i]:
            exportData += j + "\n"
        with open(output+"/as"+i,"w") as f:
            f.write(exportData)
            f.close()
    print("All jobs are done and successful ! ")
        
if __name__ == '__main__':
    main([sys.argv[1],sys.argv[2]],sys.argv[3])
