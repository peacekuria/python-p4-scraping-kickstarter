
from lib.kickstarter_scraper import create_project_dict

def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1==1

def test_scraper_returns_dict():
    """Test that scraper returns a dictionary"""
    projects = create_project_dict()
    assert isinstance(projects, dict)
    assert len(projects) > 0
