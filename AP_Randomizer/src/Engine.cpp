#pragma once
#include "Engine.hpp"

namespace Pseudoregalia_AP {
	void Engine::ExecuteInGameThread(void (*function)(UObject*) ) {
		function_queue.push_back(function);
	}

	void Engine::OnTick(UObject* blueprint) {
		for (auto& function : function_queue) {
			function(blueprint);
		}
	}

	void Engine::SyncItems() {
		auto item_sync = [](UObject* blueprint) {
			// do item sync stuff
			};

		ExecuteInGameThread(item_sync);
	}
}