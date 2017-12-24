import sys
import glob

def main():
    script = sys.argv[0]
    assert len(sys.argv) >= 2, script+" takes one ore more arguments"
    suffixes = sys.argv[1:]
    for suffix in suffixes:
        globInput = "*."+suffix
        globOutput = sorted(glob.glob(globInput))
        if len(globOutput) > 0:
            print("."+suffix+": ")
            for item in globOutput:
                print(item)
            print()

if __name__ == "__main__":
    main()
