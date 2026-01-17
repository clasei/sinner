"""
Simple sanity tests for sinner v0.1
Run without LLM to test structure and imports.
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from src import __version__
        print(f"✓ Package version: {__version__}")
    except ImportError as e:
        print(f"✗ Failed to import package: {e}")
        return False
    
    try:
        from src.core import Controller, LLMClient
        print("✓ Core modules imported")
    except ImportError as e:
        print(f"✗ Failed to import core: {e}")
        return False
    
    try:
        from src.core import prompts
        print("✓ Prompts module imported")
    except ImportError as e:
        print(f"✗ Failed to import prompts: {e}")
        return False
    
    try:
        from src.utils import GitIntegration, show_banner
        print("✓ Utils modules imported")
    except ImportError as e:
        print(f"✗ Failed to import utils: {e}")
        return False
    
    try:
        from src import cli
        print("✓ CLI module imported")
    except ImportError as e:
        print(f"✗ Failed to import CLI: {e}")
        return False
    
    return True


def test_controller_routing():
    """Test controller command routing without LLM."""
    print("\nTesting controller routing...")
    
    from src.core import Controller
    
    controller = Controller()
    
    # Test invalid command
    try:
        controller.run("invalid_command", "test")
        print("✗ Should have raised ValueError for invalid command")
        return False
    except ValueError as e:
        if "Unsupported command" in str(e):
            print(f"✓ Invalid command handled correctly")
        else:
            print(f"✗ Wrong error message: {e}")
            return False
    
    return True


def test_prompts():
    """Test prompt generation."""
    print("\nTesting prompts...")
    
    from src.core import prompts
    
    # Test each prompt function
    try:
        prompt = prompts.prompt_name("test context")
        assert len(prompt) > 0
        assert "test context" in prompt
        print("✓ prompt_name works")
        
        prompt = prompts.prompt_commit("test changes")
        assert len(prompt) > 0
        assert "test changes" in prompt
        print("✓ prompt_commit works")
        
        prompt = prompts.prompt_comment_squash(["commit1", "commit2"])
        assert len(prompt) > 0
        assert "commit1" in prompt
        print("✓ prompt_comment_squash works")
        
        prompt = prompts.prompt_comment_merge(["commit1", "commit2"])
        assert len(prompt) > 0
        assert "commit1" in prompt
        print("✓ prompt_comment_merge works")
        
        prompt = prompts.prompt_explain("test code")
        assert len(prompt) > 0
        assert "test code" in prompt
        print("✓ prompt_explain works")
        
        return True
    except Exception as e:
        print(f"✗ Prompt test failed: {e}")
        return False


def test_git_integration():
    """Test git integration (if in a repo)."""
    print("\nTesting git integration...")
    
    from src.utils import GitIntegration
    
    # Test is_git_repo
    is_repo = GitIntegration.is_git_repo()
    print(f"✓ is_git_repo returned: {is_repo}")
    
    if is_repo:
        try:
            commits = GitIntegration.get_recent_commits(count=3)
            print(f"✓ Retrieved {len(commits)} commits")
            if commits:
                print(f"  Most recent: {commits[0][:50]}...")
        except Exception as e:
            print(f"✗ get_recent_commits failed: {e}")
            return False
    
    return True


def test_banner():
    """Test banner display."""
    print("\nTesting banner...")
    
    from src.utils import show_banner
    
    try:
        show_banner()
        print("✓ Banner displayed")
        return True
    except Exception as e:
        print(f"✗ Banner failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("SINNER v0.1 SANITY TESTS")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_controller_routing,
        test_prompts,
        test_git_integration,
        test_banner,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\n✗ Test crashed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("\n🎾 All tests passed! Ready to ship v0.1")
        return 0
    else:
        print(f"\n⚠️  {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
