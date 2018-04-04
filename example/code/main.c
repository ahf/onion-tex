static int run_main_loop_once(void)
{
  int loop_result;

  // ...

  loop_result = event_base_loop(tor_libevent_get_base(),
                                called_loop_once ? EVLOOP_ONCE : 0);

  if (get_options()->MainloopStats) {
    /* Update our main loop counters. */
    if (loop_result == 0) {
      // The call was successful.
      increment_main_loop_success_count();
    } else if (loop_result == -1) {
      // The call was erroneous.
      increment_main_loop_error_count();
    } else if (loop_result == 1) {
      // The call didn't have any active or pending events
      // to handle.
      increment_main_loop_idle_count();
    }
  }

  // ...
}
