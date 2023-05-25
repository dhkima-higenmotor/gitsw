import pygit2
import csv

class config:
    def __init__(self, cfilepath):
        self.cfilepath = "D:\\github\\gitsw\\conf.csv"

    def read(self):
        data = list()
        f = open(self.cfilepath,'r')
        rea = csv.reader(f)
        for row in rea:
            data.append(row)
        f.close
        return data

# print percent
class MyRemoteCallbacks(pygit2.RemoteCallbacks):
    def transfer_progress(self, stats):
        percent = int(100.0*float(stats.indexed_objects)/float(stats.total_objects))
        print(f"# Progress : {percent} %", end="\r")

class mygit:
    def __init__(self, server, organ, user, email, token, root, exepath, gitpath, swpath):
        self.server  = "github.com"
        self.organ   = "mech-higenmotor"
        self.user    = "dhkima-higenmotor"
        self.email   = "dhkima@higenmotor.com"
        self.token   = "Copy here Github Personal Access Token."
        self.root    = "D:\\github"
        self.exepath = "D:\\github\\gitsw"
        self.gitpath = "C:\\Users\\dhkima\\scoop\\apps\\git\\current\bin"
        self.swpath  = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS"
        
    def clone(self, repo, commit_message):
        REMOTE = f"https://{self.server}/{self.organ}/{repo}.git"
        LOCAL = f"{self.root}\\{repo}"
        print(f"\n# Clone {REMOTE} Starts ...")
        pygit2.clone_repository(REMOTE, LOCAL, callbacks=MyRemoteCallbacks())
        print(f"\n# Clone into {LOCAL} Finished.")
        return 1
        
    def check_repo(self, repo):
        LOCAL = f"{self.root}\\{repo}"
        if pygit2.discover_repository(LOCAL) == None:
            print("No repo")
            return 0
        else:
            print("Good")
            return 1

    # List of All branches
    def listall_branch(self, repo):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        LISTALL_BRANACH = REPO.listall_branches()
        print(LISTALL_BRANCH)
        return LISTALL_BRANCH
        
    # Check branch existing
    def check_branch(self, repo, branch):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        if REPO.branches.get(REPO) is None:
            print("No branch")
            return 0
        else:
            print("Good")
            return 1

    # Create a local branch
    def create_branch(self, repo, branch):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        REPO.create_branch(branch, REPO.head.peel(), True)

    # checkout new branch
    def checkout_branch(self, repo, branch):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        REPO.checkout(f"refs/heads/{branch}")
        
    # Get current branch
    def current_branch(self, repo):
        LOCAL = f"{self.root}\\{repo}"
        CURRENT_BRANCH = pygit2.Repository(LOCAL,pygit2.GIT_BRANCH_LOCAL).head.shorthand
        return CURRENT_BRANCH

    # List of status
    def list_mfiles(self, repo):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        status = REPO.status()
        mfiles = list(status.keys())
        print(mfiles)
        return mfiles

    # add
    def add(self, repo, addfiles):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        index = REPO.index
        for path in addfiles:
            index.add(path)
            index.write()

    # commit
    def commit(self, repo, branch, message):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        ref = REPO.head.name
        author = pygit2.Signature(self.user, self.email)
        committer = pygit2.Signature(self.user, self.email)
        tree = index.write_tree()
        parents = [REPO.head.target]
        REPO.create_commit(ref, author, committer, message, tree, parents)

    # merge and commit
    def merge(self, repo, branch):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        branch = REPO.lookup_branch(branch, pygit2.GIT_BRANCH_LOCAL)
        oid = branch.target
        REPO.merge(oid, favor='theirs')
        # commit
        ref = "HEAD"
        author = pygit2.Signature(self.user, self.email)
        committer = pygit2.Signature(self.user, self.email)
        message = f"Merged from {branch} : {oid}"
        tree = index.write_tree()
        parents = [REPO.head.target, oid]
        REPO.create_commit(ref, author, committer, message, tree, parents)

    # push
    def push(self, repo, branch):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        remote = REPO.remotes["origin"]
        callbacks = pygit2.RemoteCallbacks(pygit2.UserPass(self.token, 'x-oauth-basic'))
        remote.push([f'refs/heads/{branch}'],callbacks=callbacks)

    # pull
    def pull(self, repo, remote_name='origin', branch='main'):
        LOCAL = f"{self.root}\\{repo}"
        REPO = pygit2.Repository(LOCAL)
        for remote in REPO.remotes:
            if remote.name == remote_name:
                remote.fetch()
                remote_master_id = REPO.lookup_reference('refs/remotes/origin/%s' % (branch)).target
                merge_result, _ = REPO.merge_analysis(remote_master_id)
                # Up to date, do nothing
                if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
                    print("\n# Up to date.")
                    return
                # We can just fastforward
                elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
                    REPO.checkout_tree(REPO.get(remote_master_id))
                    try:
                        master_ref = REPO.lookup_reference('refs/heads/%s' % (branch))
                        master_ref.set_target(remote_master_id)
                    except KeyError:
                        REPO.create_branch(branch, REPO.get(remote_master_id))
                    REPO.head.set_target(remote_master_id)
                elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
                    REPO.merge(remote_master_id)
                    if REPO.index.conflicts is not None:
                        for conflict in REPO.index.conflicts:
                            print('Conflicts found in:'+conflict[0].path)
                        raise AssertionError('Conflicts, ahhhhh!!')
                    user = REPO.default_signature
                    tree = REPO.index.write_tree()
                    commit = REPO.create_commit('HEAD', user, user, 'Merge!', tree, [repo.head.target, remote_master_id])
                    # We need to do this or git CLI will think we are still merging.
                    REPO.state_cleanup()
                else:
                    raise AssertionError('Unknown merge analysis result')
