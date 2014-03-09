from keybench.main.core import run

class KBBenchmark(object):
  """The executor of a set of runs.

  The executor of a runs specified by names. No instance should be created,
  instead C{KBBenchmark.singleton()} must be called.

  Attributes:
    run_configurations: The run configurations (C{map} of C{string} name keys
      and C{KBComponentFactory} values).
  """

  __singleton_instance = None

  @classmethod
  def singleton(cls):
    if cls.__singleton_instance == None:
      cls.__singleton_instance = KBBenchmark()
    return cls.__singleton_instance

  def __init__(self):
    super(KBBenchmark, self).__init__()

    self._run_configurations = {}

  @property
  def run_configurations(self):
    return self._run_configurations

  @run_configurations.setter
  def run_configurations(self, value):
    self._run_configurations = value

  def start(self):
    """Executes every run.
    """

    for run_name in self._run_configurations:
      run = run.KBRun(run_name)

      run.start()
